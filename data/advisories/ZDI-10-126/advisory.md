# ZDI-10-126: Ipswitch Imail Server List Mailer Reply-To Address Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-126
- **ZDI-CAN:** ZDI-CAN-736
- **Date:** 2010-07-15
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Ipswitch
- **Affected Products:** IMail
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-126/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IPSwitch IMail List Mailer. Authentication is not required to exploit this vulnerability. The specific flaw exists within imailsrv.exe which is invoked to handle messages sent to the imailsrv. When a message contains multiple "Reply-To:" headers the imailsrv.exe process concatenates these into a single fixed length buffer on the stack. No validation of the data or data length is done. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Update to the latest version 11.02

## Disclosure Timeline

- 2010-06-08 - Vulnerability reported to vendor
- 2010-07-15 - Coordinated public release of advisory
