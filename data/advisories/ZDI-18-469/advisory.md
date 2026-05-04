# ZDI-18-469: Trend Micro Endpoint Application Control FileDrop Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-469
- **ZDI-CAN:** ZDI-CAN-5640
- **Date:** 2018-05-17
- **CVE:** CVE-2018-10357
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Endpoint Application Control
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-469/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Endpoint Application Control. Authentication is required to exploit this vulnerability. The specific flaw exists within the FileDrop servlet. When parsing filenames, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code under the context of administrator.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119811

## Disclosure Timeline

- 2018-02-02 - Vulnerability reported to vendor
- 2018-05-17 - Coordinated public release of advisory
- 2018-05-17 - Advisory Updated
