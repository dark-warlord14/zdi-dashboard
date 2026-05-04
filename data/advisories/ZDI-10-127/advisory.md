# ZDI-10-127: Ipswitch Imail Server Mailing List Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-127
- **ZDI-CAN:** ZDI-CAN-737
- **Date:** 2010-07-15
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Ipswitch
- **Affected Products:** IMail
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-127/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IPSwitch IMail. Authentication might be required to exploit this vulnerability. The specific flaw exists within imailsrv.exe which is invoked to handle messages sent to the imailsrv. When a message subject contains a "?Q?" operator the string following that sequence is copied to a local stack buffer. No validation of the data or data length is done. In order to reach this code path a mailing list must be password protected (authentication required) or have previously had a password configured (no authentication required). A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Update to the latest version 11.02

## Disclosure Timeline

- 2010-06-08 - Vulnerability reported to vendor
- 2010-07-15 - Coordinated public release of advisory
