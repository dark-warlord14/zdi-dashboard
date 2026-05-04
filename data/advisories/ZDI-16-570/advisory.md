# ZDI-16-570: Novell NetIQ Sentinel Commons DiskFileItem Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-570
- **ZDI-CAN:** ZDI-CAN-3837
- **Date:** 2016-10-17
- **CVE:** CVE-2016-1000031
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** NetIQ Sentinel
- **Credit:** Jacob Baines Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-570/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell NetIQ Sentinel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the insufficient blacklisting of certain Java objects. The issue lies in the failure to properly validate user-supplied data which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.netiq.com/support/kb/doc.php?id=7018113

## Disclosure Timeline

- 2016-06-30 - Vulnerability reported to vendor
- 2016-10-17 - Coordinated public release of advisory
