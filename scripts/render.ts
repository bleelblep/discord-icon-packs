// Render mapping.json into Themes+-layout packs: <out>/<id>/<ICON_FOLDER>/<Name>.png, 72x72, white.
import { Resvg } from '@resvg/resvg-js'
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs'

const ICON_FOLDER = 'design/components/Icon/native/redesign/generated/images'
const SIZE = 72
const [setsDir, mappingPath, outDir] = process.argv.slice(2)
const mapping: Record<string, Record<string, string>> = JSON.parse(readFileSync(mappingPath, 'utf8'))
const LAYERED = [
	'CircleCheckIcon', 'CircleErrorIcon', 'CircleExclamationPointIcon', 'CircleInformationIcon', 'CircleMinusIcon',
	'CirclePlayIcon', 'CirclePlusIcon', 'CircleQuestionIcon', 'CircleWarningIcon', 'CircleXIcon',
]

function iconSvg(set: any, name: string, size = SIZE, x = 0, y = 0): string {
	let transform = ''
	let icon = set.icons[name]
	const alias = set.aliases?.[name]
	if (!icon && alias) {
		icon = set.icons[alias.parent]
		const w0 = alias.width ?? icon.width ?? set.width ?? 16
		const h0 = alias.height ?? icon.height ?? set.height ?? 16
		const t: string[] = []
		if (alias.hFlip) t.push(`translate(${w0} 0) scale(-1 1)`)
		if (alias.vFlip) t.push(`translate(0 ${h0}) scale(1 -1)`)
		if (alias.rotate) t.push(`rotate(${alias.rotate * 90} ${w0 / 2} ${h0 / 2})`)
		transform = t.join(' ')
	}
	const w = icon.width ?? set.width ?? 16
	const h = icon.height ?? set.height ?? 16
	const left = icon.left ?? set.left ?? 0
	const top = icon.top ?? set.top ?? 0
	// Mask ids must be unique across a contact sheet.
	const body = String(icon.body).replace(/(id="|url\(#)([^")]+)/g, (_m, a, b) => `${a}${b}-${name}-${x}-${y}`)
	return `<svg x="${x}" y="${y}" width="${size}" height="${size}" viewBox="${left} ${top} ${w} ${h}" color="#ffffff"><g${transform ? ` transform="${transform}"` : ''}>${body}</g></svg>`
}

function png(svg: string, width: number): Buffer {
	return new Resvg(svg, { fitTo: { mode: 'width', value: width }, font: { loadSystemFonts: true } }).render().asPng()
}

const empty = png(`<svg xmlns="http://www.w3.org/2000/svg" width="${SIZE}" height="${SIZE}"></svg>`, SIZE)

for (const [prefix, map] of Object.entries(mapping)) {
	const set = JSON.parse(readFileSync(`${setsDir}/${prefix}.json`, 'utf8'))
	const dir = `${outDir}/packs/${prefix}/${ICON_FOLDER}`
	mkdirSync(dir, { recursive: true })
	const tree: string[] = []
	const put = (file: string, data: Buffer) => {
		writeFileSync(`${dir}/${file}`, data)
		tree.push(`${ICON_FOLDER}/${file}`)
	}
	for (const [discord, name] of Object.entries(map)) {
		const image = png(`<svg xmlns="http://www.w3.org/2000/svg" width="${SIZE}" height="${SIZE}">${iconSvg(set, name)}</svg>`, SIZE)
		put(`${discord}.png`, image)
		if (LAYERED.includes(discord)) {
			put(`${discord}-primary.png`, image)
			put(`${discord}-secondary.png`, empty)
		}
	}
	mkdirSync(`${outDir}/trees`, { recursive: true })
	writeFileSync(`${outDir}/trees/${prefix}.txt`, `${tree.sort().join('\n')}\n`)

	// Contact sheet for review: icon + Discord name + chosen name, on dark grey.
	const entries = Object.entries(map)
	const cols = 8
	const cw = 170
	const ch = 90
	const rows = Math.ceil(entries.length / cols)
	const cells = entries
		.map(([discord, name], i) => {
			const x = (i % cols) * cw
			const y = Math.floor(i / cols) * ch
			return `${iconSvg(set, name, 40, x + 65, y + 6)}<text x="${x + cw / 2}" y="${y + 62}" font-size="11" fill="#ddd" text-anchor="middle" font-family="Arial">${discord.replace(/Icon$/, '')}</text><text x="${x + cw / 2}" y="${y + 77}" font-size="10" fill="#8ab4f8" text-anchor="middle" font-family="Arial">${name}</text>`
		})
		.join('')
	const sheet = `<svg xmlns="http://www.w3.org/2000/svg" width="${cols * cw}" height="${rows * ch}"><rect width="100%" height="100%" fill="#26272b"/>${cells}</svg>`
	mkdirSync(`${outDir}/sheets`, { recursive: true })
	writeFileSync(`${outDir}/sheets/${prefix}.png`, png(sheet, cols * cw))
	console.log(prefix, tree.length, 'files')
}
