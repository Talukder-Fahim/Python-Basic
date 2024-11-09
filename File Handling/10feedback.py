def feedback_analysis():
    with open('feedback.txt','r') as rf:
        lines = rf.readlines()
        pos_count = 0
        neg_count = 0
        total_feedbacks = len(lines)
        
        for line in lines:
            if ('Positive' ) in line:
                pos_count += 1
            
            elif ('Negative' ) in line:
                neg_count += 1

        
        print(f'Total feedbacks {total_feedbacks}\nCount of positive feedbacks {pos_count}\nCount of negative feedbacks {neg_count} ')

feedback_analysis()