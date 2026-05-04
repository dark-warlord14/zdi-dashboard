# ZDI-21-485: (0Day) Siemens JT2Go DXF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-485
- **ZDI-CAN:** ZDI-CAN-11915
- **Date:** 2021-04-28
- **CVE:** CVE-2021-31784
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-485/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DXF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/25/20 - ZDI reported the vulnerability to ICS-CERT 09/28/20 - ICS-CERT confirmed receipt of the report 12/17/20 - ICS-CERT communicated that the issue is in a third-party component 01/21/21 - ICS-CERT requested an extension 01/22/21 - ZDI agreed to an extension until 02/09/21 02/05/21 - ICS-CERT requested technical clarification 02/05/21 - ZDI provided additional evidence 02/24/21 - ZDI requested an update 03/22/21 - ICS-CERT requested technical clarification 03/24/21 - ZDI provided additional evidence 04/21/21 - ZDI notified ICS-CERT of the intention to publish the report as a 0-day advisory on 04/27/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-09-25 - Vulnerability reported to vendor
- 2021-04-28 - Coordinated public release of advisory
