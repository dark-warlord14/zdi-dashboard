# ZDI-21-878: (0Day) Autodesk Meshmixer 3MF File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-878
- **ZDI-CAN:** ZDI-CAN-13170
- **Date:** 2021-07-19
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** Meshmixer
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-878/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk Meshmixer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of 3MF files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/03/21 – ZDI reported the vulnerability to the vendor 07/05/21 – ZDI requested an update 07/08/21 – ZDI requested an update 07/08/21 – The vendor communicated that they won’t fix the issue 07/09/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 07/19/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-03-03 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
