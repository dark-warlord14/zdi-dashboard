# ZDI-11-294: Symantec IM Manager ProcessAction Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-294
- **ZDI-CAN:** ZDI-CAN-1091
- **Date:** 2011-10-18
- **CVE:** CVE-2011-0554
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** IM Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-294/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec IM Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Symantec IM Manager web interface exposed by default on TCP port 80. The code in the file '\Program Files\Symantec\IMManager\IMLogWeb\rdprocess.aspx' and in underlying binary objects does not validate or sanitize the rdProcess variable when parsing requests. As a result, the variable can be redirected to untrusted remote network shares. Since the code rdServer.ActionProcessor.ProcessAction() parses operations from the contents of the file pointed to by this variable, a remote attacker can abuse this behavior (and additional vulnerabilities) to execute arbitrary commands with the privileges of target web server, usually NETWORK SERVICE.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2011&suid=20110929_00

## Disclosure Timeline

- 2011-04-06 - Vulnerability reported to vendor
- 2011-10-18 - Coordinated public release of advisory
