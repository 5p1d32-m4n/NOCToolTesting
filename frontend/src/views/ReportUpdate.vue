<template>
    <div class="container">
        <form @submit.prevent="onSubmi">
            <div class="card">
                <div class="card-header">Formulario de Reporte Inicial de Averia</div>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "ReportUpdate",
    data(){
        return{
            report_content: null,
            error: null
        }
    },
    methods:{
        onSubmit(){
            if(!this.report_content){
                this.error = "You cannot send an empty report."
            }
            
        }
    },
    created() {
        
    }
}
</script>