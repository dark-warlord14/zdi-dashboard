# ZDI-20-906: (0Day) Microsoft Windows hevcdecoder_store HEIC File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-906
- **ZDI-CAN:** ZDI-CAN-10686
- **Date:** 2020-07-20
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdul-Aziz Hariri of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-906/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of HEIC files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/05/20 - ZDI reported the vulnerability to the vendor 03/05/20 - The vendor confirmed receipt of the report 07/06/20 - ZDI requested an update 07/07/20 - The vendor considered this of moderate severity and mentioned that they will fix it in the next version release 07/08/20 - The vendor provided analysis of the report 07/09/20 - ZDI notified the vendor of the intention to publish this report as 0-day advisory on 07/20/20 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-03-05 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
