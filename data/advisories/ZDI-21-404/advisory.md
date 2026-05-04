# ZDI-21-404: (0Day) Siemens Solid Edge Viewer PAR File Parsing Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-404
- **ZDI-CAN:** ZDI-CAN-11919
- **Date:** 2021-04-13
- **CVE:** CVE-2020-26997
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-404/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PAR files. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/06/20 – ZDI reported the vulnerability to ICS-CERT 10/06/20 – ICS-CERT acknowledged the report 11/30/20 – ICS-CERT requested technical clarification (could not repro) 12/01/20 – ZDI provided additional evidence 12/01/20 – ICS-CERT requested technical clarification 12/02/20 – ZDI provided additional evidence 12/03/20 – ICS-CERT requested technical clarification 12/07/20 – ZDI provided additional evidence 12/08/20 – ICS-CERT confirmed vendor could repro the issue 12/11/20 – ICS-CERT requested technical clarification 01/13/21 – ZDI provided additional evidence 02/02/21 – ICS-CERT confirmed the vendor was working on a fix and requested an extension until March 02/02/21 – ZDI said an extension could not be provided 02/23/21 – ZDI requested an update 02/24/21 – ICS-CERT mentioned a new release was due on March 9th 03/17/21 – ICS-CERT mentioned the update did not include the case 03/17/21 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory 03/22/21 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 03/25/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-10-06 - Vulnerability reported to vendor
- 2021-04-13 - Coordinated public release of advisory
