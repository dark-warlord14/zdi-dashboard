# ZDI-17-953: NetGain Enterprise Manager RMI Registry Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-953
- **ZDI-CAN:** ZDI-CAN-4753
- **Date:** 2017-12-13
- **CVE:** CVE-2017-17406
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** Jacob Baines - Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-953/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Netgain Enterprise Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within an exposed RMI registry, which listens on TCP ports 1800 and 1850 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-07-05 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
