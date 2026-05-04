# ZDI-24-1697: XWiki.org XWiki SolrSearchMacros text Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1697
- **ZDI-CAN:** ZDI-CAN-23994
- **Date:** 2024-12-19
- **CVE:** CVE-2025-24893
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** XWiki.org
- **Affected Products:** XWiki
- **Credit:** John Kwak of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1697/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of XWiki.org XWiki. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the text parameter provided to the SolrSearchMacros endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

This vulnerability has been patched in XWiki 15.10.11, 16.4.1 and 16.5.0RC1: https://www.xwiki.org/xwiki/bin/view/TestReports/

## Disclosure Timeline

- 2024-05-06 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2025-02-03 - Advisory Updated
