######
start_block = 'block_start'
end_block = 'block_end'


# Requeriments: lines, line_num, current... results.
def main(lines, line_num, current, results):
    if start_block in current:
        out = dict()
        nline = 0
        for line in lines:
            nline += 1
            if nline < line_num:
                continue
            if end_block in line:
               break
            if nline == line_num:
                out["type"] = "block"
            else:
                propert = line.partition('=')[0]
                propert = propert.strip()
                propert = propert.strip("'")
                value = line.partition('=')[2]
                value = value.strip()
                value = value.strip("'")
                out[propert] = value
        results.append(out)
        # Make sure the end_block exist
        if not (end_block in line):
            raise ValueError('Lines out of boundaries..')
