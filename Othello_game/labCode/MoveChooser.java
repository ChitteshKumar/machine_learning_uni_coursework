import java.util.ArrayList; 
import java.util.Collections; 



public class MoveChooser {
    static int valueWeights[][] = {{120 ,-20 ,20 ,5 ,5 ,20 ,-20 ,120},
            {-20 ,-40 ,-5 ,-5 ,-5 ,-5 ,-40 ,-20},
            {20 ,-5 ,15 ,3, 3, 15 ,-5 ,20},
            {5 ,-5 ,3 ,3 ,3 ,3 ,-5 ,5},
            {5 ,-5 ,3 ,3 ,3,3 ,-5 ,5},
            {20 ,-5 ,15 ,3 ,3 ,15, -5 ,20},
            {-20 ,-40 ,-5 ,-5 ,-5 ,-5 ,-40 ,-20},
            {120 ,-20 ,20 ,5 ,5 ,20 ,-20, 120}};

    
    public static Move chooseMove(BoardState boardState){
        
        
    int searchDepth = Othello.searchDepth;
        ArrayList<Move> moves= boardState.getLegalMoves();
        int finalPos = 0;
        int conclusion = 0;
        
        if(moves.isEmpty()){
            return null;
            }
        else {
            conclusion = miniMaxWP(searchDepth,-1500,1500,boardState);   // large value of aplha and beta are taken to depict inifnity 
            for(int i = 0; i < moves.size();i++) {
                    int ycoor = moves.get(i).y;
                    int xcoor = moves.get(i).x;
                    
                    if(conclusion >= valueWeights[xcoor][ycoor])break;
           
            }
            for(int i =0; i< moves.size();i++) {
                if(valueWeights[moves.get(i).x][moves.get(i).y] == conclusion){
                    finalPos =i;
                    break;
                } 
            }
            return moves.get(finalPos);  
        }    
    
    }
    
    // mini max algorithm with alpha beta pruning 
    public static int miniMaxWP(int Depth, int Alpha, int Beta,BoardState boardstate) {
        
        ArrayList<Move> moves= boardstate.getLegalMoves();
        int set=0;
        if(moves.isEmpty() && boardstate.gameOver() == false)
            {
            boardstate.colour = 1;
            return miniMaxWP(Depth, Alpha, Beta, boardstate);
            }
            
        if(Depth == 0) return staticEvaluation(boardstate);
        else if(boardstate.colour == 1){
            Alpha = -1000;            
            for(int i = 0;i < moves.size(); i++){
                BoardState boardstate1 = boardstate.deepCopy();
                boardstate1.makeLegalMove(moves.get(i).x, moves.get(i).x);
                int res = miniMaxWP(Depth-1, Alpha, Beta, boardstate);
                Alpha = Math.max(Alpha,res);
                if(Beta <= Alpha) {
                    break;
                }  
            }
            set = Alpha;
        }

        else if(boardstate.colour == -1){
            Beta = 1000;
            for(int i = 0;i < moves.size(); i++){
                BoardState boardstate1 = boardstate.deepCopy();
                boardstate1.makeLegalMove(moves.get(i).x, moves.get(i).x);
                int res = miniMaxWP(Depth-1, Alpha, Beta, boardstate);
                Beta = Math.min(Beta,res);
                if(Beta <= Alpha){
                    break; 
                } 
            }   
            set= Beta;
    }
        return set;
        
}
   
     // function to calculate  static eval function 
   public static int staticEvaluation(BoardState boardstate) {          
       int white = 0; 
       int black = 0; 
       int board;
       int piece_colour;
       for(int i = 0; i < 8; i++) {
           for(int j = 0; j < 8; j++) {
               piece_colour = boardstate.getContents(i, j);
               if(piece_colour == 1) white += valueWeights[i][j];
               if(piece_colour == -1)black += valueWeights[i][j];
           }
       }
       board = white - black;
       return board;
       
       

       
       

    }
        
   
}