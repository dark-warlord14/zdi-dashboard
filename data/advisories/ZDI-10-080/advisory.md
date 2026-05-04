# ZDI-10-080: HP Mercury LoadRunner Agent Trusted Input Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-080
- **ZDI-CAN:** ZDI-CAN-177
- **Date:** 2010-05-06
- **CVE:** CVE-2010-1549
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-080/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Mercury LoadRunner. Authentication is not required to exploit this vulnerability. The specific flaw exists within the process magentproc.exe that binds to TCP port 54345. A specially crafted packet will allow unauthenticated users to execute local commands. When a state of 0 or 4 is passed after the parameters, mchan.dll will process the commands on the host. This allows for remote code execution under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c00912968

## Disclosure Timeline

- 2007-03-19 - Vulnerability reported to vendor
- 2010-05-06 - Coordinated public release of advisory
