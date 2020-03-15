import pickle
import squad_metrics

def main():

    f = open(r'examples', 'rb')
    examples = pickle.load(f)
    f.close()

    f = open(r'predictions', 'rb')
    predictions = pickle.load(f)
    f.close()

    result = squad_metrics.squad_evaluate(examples, predictions)

    result = dict((k, v) for k, v in result.items())
    print(result)

    # print(sorted([len(example.context_text.split()) for example in examples]))

if __name__ == "__main__":
    main()
