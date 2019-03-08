import argparse
import json

from src.cluster_maker import makeCluster


def main(input_file, output_file, cluster_on, cluster_number, pretty=False):
    with open(input_file, 'r') as f:
        json_data = json.loads(f.read())
        clusters = makeCluster(json_data, cluster_on, cluster_number)
        with open(output_file, 'w') as w:
            if pretty:
                json.dump(clusters, indent=4, sort_keys=True, fp=w)
            else:
                json.dump(clusters, fp=w)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a clustering of a list of bike stations.')
    parser.add_argument('--input-file', '-f', type=str, required=True,
                        help='the json input file containing the list of bike stations.')
    parser.add_argument('--pretty', '-p', action="store_true",
                        help='outputs prettified clusters.')
    parser.add_argument('-c', '--cluster-on', type=str, choices=['position'], required=False, default='position',
                        help='what should be used to discriminate between clusters, \'position\' is the only supported'
                             'value for now.')
    parser.add_argument('-n', '--cluster-number', type=int, required=False, default=3,
                        help='number of clusters to output (default 3).')
    parser.add_argument('-o', '--output-file', type=str, required=False, default='data/clusters_result.json',
                        help='output destination file (default: data/clusters_result.json).')
    args = parser.parse_args()
    main(args.input_file, args.output_file, args.cluster_on, args.cluster_number, args.pretty)
