package me.pe4en1e.WalkieTalkieAuthService;


import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RequestController {

    @RequestMapping("/")
    public ResponseEntity test() {
        try {
            return ResponseEntity.ok("OK!");
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Error!");
        }
    }

}
