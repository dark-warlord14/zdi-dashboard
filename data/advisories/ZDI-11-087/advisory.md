# ZDI-11-087: Novell iPrint LPD Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-087
- **ZDI-CAN:** ZDI-CAN-1008
- **Date:** 2011-02-16
- **CVE:** CVE-2010-4328
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Francis Provencher for Protek Research Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-087/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Server. Authentication is not required to exploit this vulnerability. The flaw exists within the '/opt/novell/iprint/bin/ipsmd' component this component communicates with 'ilprsrvd' which listens on TCP port 515. When handling multiple LPR opcodes the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the iprint user.

## Additional Details

http://download.novell.com/Download?buildid=KloKR_CmrBs~ The problem is documented in Novell TID 7007858.

## Disclosure Timeline

- 2010-12-01 - Vulnerability reported to vendor
- 2011-02-16 - Coordinated public release of advisory
