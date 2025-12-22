#!/bin/bash

# updates system packages 
package() {
	sudo apt update -y
	sudo apt upgrade -y
}

package
