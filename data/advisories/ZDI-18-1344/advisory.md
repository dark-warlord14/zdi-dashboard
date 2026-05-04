# ZDI-18-1344: Apple macOS usymptomsd Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1344
- **ZDI-CAN:** ZDI-CAN-6350
- **Date:** 2018-11-05
- **CVE:** CVE-2018-4203
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Bruno Keith (@bkth_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1344/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the usymptomsd service. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code within the context of the symptomsd process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-06-14 - Vulnerability reported to vendor
- 2018-11-05 - Coordinated public release of advisory
- 2018-11-05 - Advisory Updated
