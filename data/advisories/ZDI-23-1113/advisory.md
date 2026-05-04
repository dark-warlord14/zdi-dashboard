# ZDI-23-1113: Schneider Electric EcoStruxure Operator Terminal Expert VXDZ File Parsing Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1113
- **ZDI-CAN:** ZDI-CAN-17204
- **Date:** 2023-08-15
- **CVE:** CVE-2023-1049
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Operator Terminal Expert
- **Credit:** Daan Keuper & Thijs Alkemade from Computest
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1113/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric EcoStruxure Operator Terminal Expert. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of of VXDZ files while in simulation mode. When parsing name:value pairs in configuation data, the process does not properly validate a user-supplied string before executing it as code. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2023-164-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2023-164-01.pdf&_ga=2.140486835.1846662606.1686683693-1425362997.1686683693 https://www.cisa.gov/news-events/ics-advisories/icsa-23-180-02

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated
