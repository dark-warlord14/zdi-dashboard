# ZDI-20-546: Veeam ONE HandshakeResult Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-546
- **ZDI-CAN:** ZDI-CAN-10401
- **Date:** 2020-04-16
- **CVE:** CVE-2020-10915
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Veeam
- **Affected Products:** ONE
- **Credit:** Michael Zanetta & Edgar Boda-Majer from Bugscale
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-546/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Veeam ONE. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HandshakeResult method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Veeam has issued an update to correct this vulnerability. More details can be found at: https://www.veeam.com/kb3144

## Disclosure Timeline

- 2020-02-26 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
- 2020-05-14 - Advisory Updated
