# ZDI-23-773: (Pwn2Own) Samsung Galaxy S22 InstantPlaysDeepLink Permissive List of Allowed Inputs Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-773
- **ZDI-CAN:** ZDI-CAN-19751
- **Date:** 2023-05-31
- **CVE:** CVE-2023-21514
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S22
- **Credit:** Chim
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-773/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Galaxy S22 smartphones. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the InstantPlaysDeepLink class. The issue results from a permissive list of allowed inputs. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
