# ZDI-15-380: Microsoft Internet Explorer Enhanced Protected Mode Read-Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-380
- **ZDI-CAN:** ZDI-CAN-2921
- **Date:** 2015-08-11
- **CVE:** CVE-2015-2429
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-380/
## Vulnerability Details

This vulnerability allows local attackers to partially escape AppContainer limitations on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the IShdocvwBroker::EditWith broker API call. The issue lies in the failure to check for registry symbolic links before recursively traversing the key. An attacker can leverage this vulnerability to read the contents of any key within the HKCU registry hive, bypassing the read restrictions designed into EPM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-090

## Disclosure Timeline

- 2015-05-07 - Vulnerability reported to vendor
- 2015-08-11 - Coordinated public release of advisory
