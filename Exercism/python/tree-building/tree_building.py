class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    records.sort(key=lambda r: r.record_id)

    if not all(r.record_id == i for i, r in enumerate(records)):
        raise ValueError(
            'record numbers must be unique and continuous starting from 0')
    if not all(r.parent_id == 0 or 0 <= r.parent_id < r.record_id for r in records):
        raise ValueError('parent id must be 0 or lower than child id')

    nodes = [Node(0)]

    for r in records[1:]:
        nodes.append(Node(r.record_id))
        nodes[r.parent_id].children.append(nodes[-1])

    return nodes[0] if records else None
