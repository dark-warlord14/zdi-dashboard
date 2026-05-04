# ZDI-10-138: Novell iPrint Server Queue Name Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-138
- **ZDI-CAN:** ZDI-CAN-742
- **Date:** 2010-08-05
- **CVE:** CVE-2010-4320
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Francis Provencher for Protek Research Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-138/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Server. Authentication is not required to exploit this vulnerability. The flaw exists within the '/opt/novell/iprint/bin/ipsmd' component this component communicates with 'ilprsrvd' which listens on TCP port 515. When handling an LPR opcode 0x01 packet type the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the iprint user.

## Additional Details

To alleviate prior incomplete patch Novell released the following updates September 14, 2010. Novell iPrint for OES2 SP2 20100730 (Architecture: x86) http://download.novell.com/Download?buildid=LOFeoNQGkRc~ Novell iPrint for OES2 SP2 20100730 (Architecture: x86-64) http://download.novell.com/Download?buildid=NEb-rQmxvpg~

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-08-05 - Coordinated public release of advisory
