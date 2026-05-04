# ZDI-21-566: (0Day) Siemens Solid Edge Viewer JT File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-566
- **ZDI-CAN:** ZDI-CAN-12084
- **Date:** 2021-05-12
- **CVE:** CVE-2021-27490
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-566/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JT files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 12/02/20 - ZDI reported the vulnerabilities to ICS-CERT 12/03/20 - ICS-CERT confirmed receipt of the report 12/08/20 - ICS-CERT communicated that the issue is in a third-party component 02/24/21 - ZDI requested an update 02/25/21 - ICS-CERT confirmed that the vendor was working on a fix 03/18/21 - ZDI requested an update 03/18/21 - ICS-CERT requested an extension 03/22/21 - ZDI agreed to an extension until 04/13/21 04/14/21 - ZDI requested an update 04/27/21 - ZDI requested an update 04/27/21 - The vendor provided CVEs for the cases 05/03/21 - ICS-CERT requested an extension until 05/25/21 05/04/21 - ZDI notified ICS-CERT of the intention to publish this report as a 0-day advisories on 05/12/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-05-12 - Coordinated public release of advisory
