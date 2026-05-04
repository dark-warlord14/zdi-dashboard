# ZDI-20-1441: (0Day) Eaton EASYsoft E70 File Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1441
- **ZDI-CAN:** ZDI-CAN-11078
- **Date:** 2020-12-15
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Eaton
- **Affected Products:** EASYsoft
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1441/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Eaton EASYsoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of E70 files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/29/20 - ZDI reported the vulnerability to ICS-CERT 08/26/20 - The vendor requested technical clarification 08/27/20 - ZDI provided additional evidence 10/05/20 - ZDI requested a status update 10/08/20 - Eaton requested an extension 10/08/20 - ZDI granted an extension until December 12/10/20 - ZDI notified ICS-CERT of the intention to publish the report as 0-day advisory on 12/15/2020 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-05-29 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
