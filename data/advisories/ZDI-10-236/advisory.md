# ZDI-10-236: SAP NetWeaver Composition Environment sapstartsrv.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-236
- **ZDI-CAN:** ZDI-CAN-896
- **Date:** 2010-11-08
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SAP
- **Affected Products:** NetWeaver
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-236/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP NetWeaver Composition Environment. Authentication is not required to exploit this vulnerability. The specific flaw exists within the sapstartsrv.exe process which listens by default on ports 50013 and 50113. A malformed SOAP request (via POST) can be used to reach an unbounded copy loop which results in attacker-supplied data being written into existing function pointers. It is possible for a remote attacker to leverage this vulnerability to execute arbitrary code.

## Additional Details

A solution was provided via SAP note 1414444 https://service.sap.com/sap/support/notes/1414444

## Disclosure Timeline

- 2010-10-18 - Vulnerability reported to vendor
- 2010-11-08 - Coordinated public release of advisory
