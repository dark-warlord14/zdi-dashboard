# ZDI-13-249: Oracle BPEL Process Manager ScriptServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-249
- **ZDI-CAN:** ZDI-CAN-1761
- **Date:** 2013-10-16
- **CVE:** CVE-2013-3828
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** BPEL Process Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-249/
## Vulnerability Details

This vulnerability allows remote attackers to obtain sensitive information on vulnerable installations of Oracle BPEL Process Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ScriptServlet. It suffers of a directory traversal vulnerability inside the query string which can lead to disclosure of credentials. By abusing this behavior an attacker can disclose administrative credentials and possibly leverage this situation to achieve remote code execution.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuoct2013-1899837.html

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory
