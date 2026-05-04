# ZDI-11-154: Sybase M-Business Anywhere agSoap.exe password Tag Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-154
- **ZDI-CAN:** ZDI-CAN-941
- **Date:** 2011-05-09
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sybase
- **Affected Products:** MBusiness Anywhere
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-154/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sybase M-Business Anywhere. Authentication is not required to exploit this vulnerability. The specific flaw exists within the gsoap.exe module exposed by the webserver that listens by default on TCP ports 8093 and 8094. A remote user can send an specially crafted SOAP packet with an invalid 'password' closing tag via a POST request to the web server to trigger a buffer overflow in this module. Exploitation of this issue leads to remote code execution under the context of the target service.

## Additional Details

Sybase has issued an update to correct this vulnerability. More details can be found at: http://www.sybase.com/detail?id=1093029

## Disclosure Timeline

- 2011-01-20 - Vulnerability reported to vendor
- 2011-05-09 - Coordinated public release of advisory
