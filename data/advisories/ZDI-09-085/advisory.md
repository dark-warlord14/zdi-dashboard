# ZDI-09-085: Hewlett-Packard Operations Manager Server Backdoor Account Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-085
- **ZDI-CAN:** ZDI-CAN-618
- **Date:** 2009-11-20
- **CVE:** CVE-2009-3843
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Operations Manager for Windows
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-085/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Operations Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists due to a hidden account present within the Tomcat users XML file. Using this account a malicious user can access the org.apache.catalina.manager.HTMLManagerServlet class. This is defined within the catalina-manager.jar file installed with the product. This servlet allows a remote user to upload a file via a POST request to /manager/html/upload. If an attacker uploads malicious content it can then be accessed and executed on the server which leads to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01931960

## Disclosure Timeline

- 2009-11-09 - Vulnerability reported to vendor
- 2009-11-20 - Coordinated public release of advisory
