# heights = [6,4,8,5,2,7]
# queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
# # heights = [5,3,8,2,6,1,4,6]
# # queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
# # heights=[1,2]
# # queries=[[0,0],[0,1],[1,0],[1,1]]
# # 0=2,1=2,2=-1,3=5,4=5,5=5
# n=len(queries)
# ans=[-1]*n
# arr=[-1]*len(heights)
# for i in range(len(heights)):
#     for j in range(i,len(heights)):
#         if heights[j]>heights[i]:
#             arr[i]=j
#             break
# print(arr)
# for i in range(len(queries)):
#     l,r=queries[i]
#     # print(l,r)
#     if l==r:
#         ans[i]=l
#     elif l<r and heights[l]<heights[r]:
#         ans[i]=r
#     elif l>r and heights[l]>heights[r]:
#         ans[i]=l
#     else:
#         maxi=max(heights[l],heights[r])
#         if maxi==heights[l]:
#             maxi_ind=l
#         else:
#             maxi_ind=r
#         if arr[maxi_ind]>min(heights[l],heights[r]):
#             ans[i]=arr[maxi_ind]
#         else:
#             ans[i]=arr[heights.index(min(heights[l],heights[r]))]
        
#         # maxi=max(heights[l],heights[r])
#         # # print(maxi)
#         # for j in range(max(l,r),len(heights)):
#         #     if heights[j]>maxi:
#         #         ans[i]=j
#         #         break
# print(ans)
# # for i,j in queries:
# #     maxi=max(heights[i],heights[j])
# #     print(maxi)
# #     for k in range(max(i,j),n):
# #         if heights[k]>maxi:
# #             ans.append(k)
# #             break
# #     ans.append(-1)
# # print(ans)
import chess
import chess.svg
from IPython.display import display, HTML

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.turn = chess.WHITE

    def print_board(self):
        display(HTML(chess.svg.board(board=self.board, size=400)))

    def move(self, move):
        try:
            chess_move = self.board.parse_san(move)
            self.board.push(chess_move)
            self.turn = not self.turn
            self.print_board()
        except ValueError:
            print("Invalid move. Please try again.")

    def is_game_over(self):
        return self.board.is_game_over()

    def get_winner(self):
        if self.board.is_checkmate():
            return "White" if self.turn == chess.BLACK else "Black"
        return "Draw"

def main():
    game = ChessGame()
    game.print_board()

    while not game.is_game_over():
        player = "White" if game.turn == chess.WHITE else "Black"
        move = input(f"{player}'s move: ")
        game.move(move)

    print("Game over!")
    winner = game.get_winner()
    if winner == "Draw":
        print("The game is a draw.")
    else:
        print(f"The winner is {winner}.")

if __name__ == "__main__":
    main()
