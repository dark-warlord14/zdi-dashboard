# ZDI-20-1439: (0Day) LibTIFF tiff2pdf Converter Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1439
- **ZDI-CAN:** ZDI-CAN-11115
- **Date:** 2020-12-15
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** LibTIFF
- **Affected Products:** LibTIFF
- **Credit:** ZhangJiaxing from Codesafe Team of Legendsec at Qi'anxin Group
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1439/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of LibTIFF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the tiff2pdf converter. Crafted data in a TIFF file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/24/20 - ZDI reported the vulnerability to the Spatialys 06/24/20 - Spatialys opened a case on https://gitlab.com/libtiff/libtiff/-/issues/194 07/10/20 - ZDI requested an update 07/10/20 - Spatialys replied that they have no interest in the issue and recommended two LibTIFF developers 07/10/20 - ZDI notified Spatialys of the intention to publish the report as 0-day advisory after 10/22/2020 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-06-24 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
