# ZDI-23-591: Trend Micro Mobile Security for Enterprises widgetforsecurity getWidgetPoolManager Local File Inclusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-591
- **ZDI-CAN:** ZDI-CAN-20181
- **Date:** 2023-05-12
- **CVE:** CVE-2023-32528
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Mobile Security for Enterprises
- **Credit:** Poh Jia Hao of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-591/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Mobile Security for Enterprises. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the getWidgetPoolManager function defined within the web/widgetforsecurity path. The issue results from the lack of proper validation of user-supplied data prior to passing it to a PHP include function. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of IUSR.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000293106

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-05-12 - Coordinated public release of advisory
