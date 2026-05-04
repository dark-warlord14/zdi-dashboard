# ZDI-17-283: Trend Micro Deep Discovery Email Inspector policy_setting Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-283
- **ZDI-CAN:** ZDI-CAN-4427
- **Date:** 2017-04-11
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Discovery Email Inspector
- **Credit:** Nikolay Klendar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-283/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Deep Discovery Email Inspector. Authentication is not required to exploit this vulnerability. The specific flaw exists within policy_setting.php. The issue results from the lack of proper validation of user-supplied data, which can allow for the upload of arbitrary files. An attacker can leverage this vulnerability to execute code under the context of the root user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117093

## Disclosure Timeline

- 2017-02-16 - Vulnerability reported to vendor
- 2017-04-11 - Coordinated public release of advisory
