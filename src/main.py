
from towel_design import design_towels


def main():
    file_path = 'input.txt'
    output, num_of_possible_designs = design_towels(file_path) 
    for output_line in output:  
        print(output_line)

    print(f'Number of possible designs: {num_of_possible_designs}')

if __name__ == "__main__":
    main()
