# ZDI-23-818: (0Day) ZTE MF286R goahead Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-818
- **ZDI-CAN:** ZDI-CAN-19059
- **Date:** 2023-06-07
- **CVE:** CVE-2023-25649
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ZTE
- **Affected Products:** MF286R
- **Credit:** Rafal Goryl (@voix44er)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-818/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of ZTE MF286R routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of a request parameter provided to the SET_DEVICE_LED endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

ZTE has issued an update to correct this vulnerability. More details can be found at: https://support.zte.com.cn/support/news/LoopholeInfoDetail.aspx?newsId=1032544

## Disclosure Timeline

- 2022-11-24 - Vulnerability reported to vendor
- 2023-06-07 - Coordinated public release of advisory
- 2023-08-31 - Advisory Updated
