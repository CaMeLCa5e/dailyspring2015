			<form method="post" action="sendemail.php" enctype="multipart/form-data">
				<label style="float: left;	">
					Your name:
				</label>
				<br>
				<input type="text" name="name" style="
					float: left;
					background-color: #AEA79F; 
					min-height: 20px;
					min-width: 200px;
					border-style: none;
					">
				</input>	
				<br>
				<br>
					<label style="float: left;">Your email:</label>
					<br>
					<input type="email" name="email" style="
						float: left;
						background-color: #AEA79F; 
						min-height: 20px;
						min-width: 200px;
						border-style: none;">
					</input>
					<br>
					<br>
					<label style="float: left;">Your message:</label>
					<br/>
					<textarea name="message" style="
						float: left; 
						background-color: #AEA79F; 
						min-width: 400px;
						min-height: 200px;
						border-style: none;">
					</textarea>
					<div class="clear"></div>
					<br>
					<label style="float: left;">Resume:</label>
					<br>
					<input type="file" name="attach1" style="float: left;"/>
					<br>
					<br>
					<input type="submit" value="submit" style="
						float: left; 
						color: #ffffff;
						background-color: #772953;
						padding: 5px 15px;
						border-style: ridge;
						border-color: #AEA79F;
						border-size: 3px;
						margin: 15px;
						font-size: 16px;
						font-weight: bold;
						margin-top: 10px;">
						</input>
				</form>