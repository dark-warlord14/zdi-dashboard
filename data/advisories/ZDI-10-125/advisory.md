# ZDI-10-125: IBM SolidDB solid.exe Handshake Request Username Field Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-125
- **ZDI-CAN:** ZDI-CAN-676
- **Date:** 2010-07-13
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** solidDB
- **Credit:** AbdulAziz Hariri and Zein Fneish Insight Technologies
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-125/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM solidDB. Authentication is not required to exploit this vulnerability. The specific flaw exists within the solid.exe process which listens by default on TCP port 1315. The code responsible for parsing the first handshake packet does not properly validate the length of the username field. By crafting an overly long value in the request an attacker can exploit this to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21439148&myns=swgimgmt&mynp=OCSSPK3V&mync=R

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-07-13 - Coordinated public release of advisory
