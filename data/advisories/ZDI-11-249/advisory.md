# ZDI-11-249: (Pwn2Own) Microsoft Internet Explorer Protected Mode Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-249
- **ZDI-CAN:** ZDI-CAN-1159
- **Date:** 2011-08-09
- **CVE:** CVE-2011-1347
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-249/
## Vulnerability Details

This vulnerability allows remote attackers to escape Protected Mode on vulnerable installations of Internet Explorer. Internet Explorer Protected Mode consists of a Medium Integrity and a Low Integrity process. The Low Integrity process is only allowed to write to special Low Integrity locations. File written there are marked as Low Integrity files. When a new Internet Explorer process is launched it checks the Integrity of the file it is launched against. If the file is a Low Integrity file it will run the process in Low Integrity Mode. It is however possible to give the file an even lower permission: Untrusted, since this does not match the check for 'Low Integrity' the Internet Explorer will run in Medium Integrity instead of Low Integrity. This can be abused in an exploit to bypass the Protected Mode design and thus allow an attacker to escalate their privileges.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS11-057.mspx

## Disclosure Timeline

- 2011-03-09 - Vulnerability reported to vendor
- 2011-08-09 - Coordinated public release of advisory
