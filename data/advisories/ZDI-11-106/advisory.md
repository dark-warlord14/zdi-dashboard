# ZDI-11-106: Novell Netware NWFTPD.NLM DELE Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-106
- **ZDI-CAN:** ZDI-CAN-940
- **Date:** 2011-03-18
- **CVE:** CVE-2010-4228
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Francis Provencher for Protek Research Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-106/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Netware. Authentication is required to exploit this vulnerability. The flaw exists within NWFTPD.NLM. When handling the argument provided to the DELE command the application copies user supplied data to a fixed length stack buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the super user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=Ax6AbxwGLTs~

## Disclosure Timeline

- 2010-09-22 - Vulnerability reported to vendor
- 2011-03-18 - Coordinated public release of advisory
