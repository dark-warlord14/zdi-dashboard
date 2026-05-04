# ZDI-11-227: Novell File Reporter Engine RECORD Tag Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-227
- **ZDI-CAN:** ZDI-CAN-1250
- **Date:** 2011-06-27
- **CVE:** CVE-2011-2220
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Novell
- **Affected Products:** File Reporter
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-227/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell File Reporter Engine. Authentication is not required to exploit this vulnerability. The specific flaw exists within NFREngine.exe which communicates with the Agent component over HTTPS on TCP port 3035. When parsing tags inside the <RECORD> element, the application lacks a size check before pushing strings to a memcpy. An attacker can leverage this to corrupt the thread's stack. This vulnerability can result in remote code execution under the context of the SYSTEM account.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=leLxi7tQACs~

## Disclosure Timeline

- 2011-05-25 - Vulnerability reported to vendor
- 2011-06-27 - Coordinated public release of advisory
