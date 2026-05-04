# ZDI-10-140: Novell iPrint Client Browser Plugin operation Parameter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-140
- **ZDI-CAN:** ZDI-CAN-754
- **Date:** 2010-08-05
- **CVE:** CVE-2010-4315
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Rodriguez Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-140/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Novell iPrint Client Browser Plugin. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within handling plugin parameters. Specifically, a long value for the operation parameter can trigger a stack-based buffer overflow. Successful exploitation leads to execution of arbitrary code under the context of the user running the browser process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=ftwZBxEFjIg~

## Disclosure Timeline

- 2010-06-02 - Vulnerability reported to vendor
- 2010-08-05 - Coordinated public release of advisory
