# ZDI-11-034: HP OpenView Performance Insight Server Backdoor Account Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-034
- **ZDI-CAN:** ZDI-CAN-606
- **Date:** 2011-01-31
- **CVE:** CVE-2011-0276
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Performance Insight
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard OpenView Performance Insight Server. Authentication is not required to exploit this vulnerability. The specific vulnerability is due to a hidden account present within the com.trinagy.security.XMLUserManager Java class. Using this account a malicious user can access the com.trinagy.servlet.HelpManagerServlet class. This is defined within the piweb.jar file installed with Performance Insight. This class exposes a doPost() method which an attacker can use to upload malicious files to the server. Accessing these files can then lead to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02695453

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2011-01-31 - Coordinated public release of advisory
