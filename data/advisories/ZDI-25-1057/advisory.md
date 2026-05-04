# ZDI-25-1057: (0Day) Microsoft Visual Studio VsDevCmd Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1057
- **ZDI-CAN:** ZDI-CAN-26574
- **Date:** 2025-12-10
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** Nitesh Surana (@_niteshsurana) & Nelson William Gamazo Sanchez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1057/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Visual Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within VsDevCmd.bat. The script launches an executable from an unsecured location. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

02/19/25 - ZDI reported the vulnerability to the vendor 02/19/25 – the vendor acknowledged the receipt of the report 03/17/25 – the vendor communicated that the reported behavior was not a vulnerability 11/26/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/10/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-02-19 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
