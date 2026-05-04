# ZDI-17-507: Mitsubishi Electric E-Designer Symbol xSize Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-507
- **ZDI-CAN:** ZDI-CAN-3804
- **Date:** 2017-08-01
- **CVE:** CVE-2017-9634
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mitsubishi Electric
- **Affected Products:** E-Designer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-507/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mitsubishi Electric E-Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of Symbol sections of a mpa (project specification) file. An value for the xSize specification will cause initialization to write outside the bounds of a heap buffer. An attacker can leverage this vulnerability to execute arbitrary code in the context of the Administrator.

## Additional Details

Mitsubishi Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-213-01

## Disclosure Timeline

- 2016-05-31 - Vulnerability reported to vendor
- 2017-08-01 - Coordinated public release of advisory
