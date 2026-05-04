# ZDI-17-949: NetGain Enterprise Manager heapdumps Remote Download Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-949
- **ZDI-CAN:** ZDI-CAN-4718
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16607
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** Jacob Baines - Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-949/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Netgain Enterprise Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within heapdumps.jsp. The issue results from the lack of proper validation of a user-supplied string before using it to download heap memory dump. An attacker can leverage this in conjunction with other vulnerabilities to disclose sensitive information in the context of the current process.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-07-05 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
