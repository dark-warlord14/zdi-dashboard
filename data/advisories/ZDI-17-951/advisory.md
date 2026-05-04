# ZDI-17-951: NetGain Enterprise Manager download Arbitrary File Download Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-951
- **ZDI-CAN:** ZDI-CAN-4750
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16609
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** Jacob Baines - Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-951/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Netgain Enterprise Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within download.jsp. The issue results from the lack of proper validation of a user-supplied string before using it to download a file. An attacker can leverage this vulnerability to expose sensitive information.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-07-05 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
