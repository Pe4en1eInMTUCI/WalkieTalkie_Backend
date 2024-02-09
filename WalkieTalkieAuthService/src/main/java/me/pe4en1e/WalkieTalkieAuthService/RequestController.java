package me.pe4en1e.WalkieTalkieAuthService;


import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")

@Tag(name = "Test RequestController", description = "Тестовый Request контроллер")
public class RequestController {

    @GetMapping("/test")
    @Operation(summary = "Тестовый метод", description = "Возвращает ту же строчку")
    public String test(String string) {
        try {
            return "You wrote " + string;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return "Error!";

        }
    }


}
