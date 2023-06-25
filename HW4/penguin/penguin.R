
library(shiny)
library(shinyWidgets)
library(palmerpenguins)
library(ggplot2)
library(dplyr)
library(magrittr)
library(DT)
x_vars =  c("bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g")
y_vars =  c("bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g")

# Define UI for application that draws a histogram
ui <- fluidPage(
    # Application title
    titlePanel("펭귄 데이터 분석"),
    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
          checkboxGroupInput(
            "s",
            label = "펭귄 종류를 선택하세요",
            choices = list('Adelie' = 'Adelie', 'Gentoo' = 'Gentoo', 'Chinstrap' = 'Chinstrap'),
            selected = 'Adelie'
          ),
          selectInput(inputId = "x_axis", label="x축을 선택하세요.", choices = x_vars,selected = "bill_length_mm"),
          selectInput(inputId = "y_axis", label = "y축을 선택하세요.", choices = y_vars,selected = "body_mass_g"),
            sliderInput("dots",
                        label="점 크기를 선택하세요",
                        min = 1,
                        max = 10,
                        value = 5)
        ),
        # Show a plot of the generated distribution
        mainPanel(
           dataTableOutput("penguins_table"),
           plotOutput("penguins_plot")
        )
    )
    
)


# Define server logic required to draw a histogram
server <- function(input, output,session) {
  
    sel_penguins <-reactive({
      penguins %>% 
        filter(species %in% input$s)
    })
    output$penguins_table <-renderDataTable({
     sel_penguins() %>% 
        datatable()
     })
    
    output$penguins_plot <- renderPlot({
      sel_penguins() %>% 
        ggplot(aes(x = !!sym(input$x_axis),
                  y = !!sym(input$y_axis), color = species ,shape =sex  )) +geom_point(size=input$dots)

    })


    
  
}

# Run the application 
shinyApp(ui = ui, server = server)
